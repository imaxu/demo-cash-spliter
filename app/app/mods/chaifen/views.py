# coding=utf-8


from flask import Flask,render_template
from . import chaifen
from .service.compute_service import ComputeService

@chaifen.route('/compute/<int:fee>/<int:amount>')
def compute(fee=None,amount=None):
    from json import dumps
    results = ComputeService().compute(fee,amount)
    return render_template("chaifen.html",results=dumps(results))
