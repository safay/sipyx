from flask import Flask, request, send_file
import plotting
import types
import inspect

app = Flask("corral")


def expose_fxns(app, module):
    def _expose(fxn):
        # given a function fxn, build a URL rule based on its name and args
        fxn_name = fxn.__name__
        url_rule = '/{}/'.format(fxn_name)
        for arg in inspect.getargspec(fxn).args:
            url_rule = url_rule + "<" + arg + ">/"
        url_rule = url_rule[:-1]
        app.add_url_rule(rule=url_rule, endpoint=fxn_name, view_func=fxn)
        return fxn
    # iterates over the objects declared in a given module, finding the functions and exposing them as endpoints
    for name in dir(module):
        obj = getattr(module, name, None)
        if isinstance(obj, types.FunctionType):
            _expose(obj)


expose_fxns(app, plotting)
