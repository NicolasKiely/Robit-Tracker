"use strict";
/**
 * Jquery plugin for client-server form validations
 * API entry points are jQuery().validator() and jQuery().validate()
 * 
 */

(function($){
  /***************************************************************************\
  | Plugin Initialization (Private API)                                       |
  \***************************************************************************/
  /* Internal plugin registry */
  var plugin = {
    /** Set to true when it is safe to call bind() on selector strings */
    canbind: false,

    /** Registry of all validator contexts */
    registry: [],

    /** Default values for validator contexts */
    validator_defaults: {
      formsel: 'form',
      multibind: false,
      logsel: '',
      logstatus: 'default'
    },

    /* Enumeration of logging statuses */
    log_status: {
      info: 'info',
      good: 'success',
      success: 'success',
      warning: 'warning',
      warn: 'warning',
      error: 'danger'
    }
  };

  /**
   * Registers context configuration with plugin
   * @param context New context config
   */
  plugin.register = function(context){
    plugin.registry.push(context);
  };

  /**
   * Registers a binding between a callback and a selection of elements
   * @param Context configuration for binding
   * @param Element selector
   * @param Callback Validation code to be called on selector
   */
  plugin.bind = function(context, selector, callback){
    if (plugin.canbind){
      /* Can directly bind a callback to the given selector */
      var els = $(selector);
      var elnum = context.__multibind__ ? els.length : 1;
      for (var i=0; i<elnum; i++){
        var binding = {
          element: els[i],
          callback: callback,
          selector: selector
        };
        context.__binding__.push(binding);

        /* Bind element updates to check context */
        var elementChangeCallback = (function (ctx, bnd){
          return function(e){
            console.log("Element "+ bnd.selector +" updated!");
            var res = bnd.callback(bnd.element);
            if (res){
              /* Error found, log it */
              plugin.log(ctx, res, plugin.log_status.error);

            } else {
              /* Error not found, check other conditions */
              plugin.attempt_unlock(ctx);
            }
          };
        })(context, binding);

        $(binding.element).on('input', elementChangeCallback);
      }

    } else {
      /* Can't bind the callback yet */
      if (selector in context.__prebinding__){
        context.__prebinding__[selector].push(callback);
      } else {
        context.__prebinding__[selector] = [callback];
      }
    }
  };

  /**
   * Logs validator-specific message
   */
  plugin.log = function(context, message, errStat){
    if ('__logger__' in context){
      $(context.__logger__.children()[0]).text(message);

      if (errStat){
        /* Set alert status of logging element */
        if ('__logstatus__' in context){
          context.__logger__.removeClass('panel-'+ context.__logstatus__);
        }
        context.__logger__.addClass('panel-'+errStat);
        context.__logstatus__ = errStat;
      }

    } else {
      /* No bound logger element, just send message to console */
      var errPrefix = errStat ? "[info] " : "["+errStat+"] ";
      console.log(errPrefix + message);
    }
  };


  /***************************************************************************\
  | Validator Context (Public API)                                            |
  \***************************************************************************/
  plugin.generate_validator_context = function(template){
    /* Register new validation instance */
    var validator_context = {
      __logsel__: plugin.validator_defaults.logsel,
      __formsel__: plugin.validator_defaults.formsel,
      __binding__: [],
      __multibind__: plugin.validator_defaults.multibind,
      __logstatus__: plugin.validator_defaults.logstatus,
      __prebinding__: {},
    };
    if (template){
      if (typeof(template) === 'string'){
        /* Interpet template strings as form selectors */
        validator_context.__formsel__ = template;

      } else {
        /* Interpret template objects as inheritable context */
        validator_context.__logsel__ = template.__logsel__ || '';
        validator_context.__formsel__ = template.__formsel__ || '';
        validator_context.__multibind__ = template.__multibind__ || '';
      }
    }
    plugin.register(validator_context);


    /**
     * Deferred binding for a list of fields
     * @param jqargs Object list of selector-callbacks for binding
     * @return Updated validator instance
     */
    validator_context.validate = (function(ctx){
      return function(jqargs){
        for (var selector in jqargs){
          plugin.bind(ctx, selector, jqargs[selector]);
        }
        return ctx;
      };
    })(validator_context);

    /**
     * Bind a logger for the current context
     * @param jqargs Selector for logging element(s)
     * @return Updated validator instance
     */
    validator_context.logger = (function(ctx){
      return function(jqargs){
        ctx.__logsel__ = jqargs;
        return ctx;
      };
    })(validator_context);

    /**
     * Turns on form multibinding
     * @return Updated validator instance
     */
    validator_context.multibind = (function(ctx){
      return function(jqargs){
        ctx.__multibind__ = true;
        return ctx;
      }
    })(validator_context);

    /**
     * Turns off form multibinding
     * @return Updated validator instance
     */
    validator_context.singlebind = (function(ctx){
      return function(jqargs){
        ctx.__multibind__ = false;
        return ctx;
      }
    })(validator_context);

    return validator_context;
  };


  /* Bind validation generators to jquery */
  var congen = plugin.generate_validator_context;
  $.fn.validator = congen;
  $.fn.validate = congen('form').logger('.log-panel').validate;


  /***************************************************************************\
  | Document Loaded                                                           |
  \***************************************************************************/
  $(document).ready(function(){
    plugin.canbind = true;

    /* Re-bind deferred callbacks */
    for (var ir in plugin.registry){
      /* For contexts in registry */
      var context = plugin.registry[ir];

      /* Bind logging elements first */
      if (context.__logsel__){
        context.__logger__ = $(context.__logsel__);
      };

      /* Bind validation callbacks next */
      for (var selector in context.__prebinding__){
        /* For unbound callback list for each selector in context */
        var callbacks = context.__prebinding__[selector];
        for (var ic in callbacks){
          /* For callback in list of callbacks */
          plugin.bind(context, selector, callbacks[ic]);
        }
      }
      /* Clear out prebinding object */
      context.__prebinding__ = {};
    }
  });

})(jQuery);
