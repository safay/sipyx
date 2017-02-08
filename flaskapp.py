from flask import Flask, request, send_file
import plotting
import types
import inspect

app = Flask("corral")


@app.route('/')
def hello_world():
    return 'Hello, World!'


def expose_fxns(app, module):
    def _expose(fxn):
        fxn_name = fxn.__name__
        url_rule = '/{}/'.format(fxn_name)
        for arg in inspect.getargspec(fxn).args:
            url_rule = url_rule + "<" + arg + ">/"
        url_rule = url_rule[:-1]
        app.add_url_rule(rule=url_rule, endpoint=fxn_name, view_func=fxn)
        return fxn
    # iterates over the objects declared in a given module
    for name in dir(module):
        obj = getattr(module, name, None)
        if isinstance(obj, types.FunctionType):
            print name, obj
            _expose(obj)


expose_fxns(app, plotting)

print app.url_map


# build a page that has each of the plots in it
