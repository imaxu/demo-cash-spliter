# coding=utf-8


from flask import Flask,session,g
from . import chaifen
from .service.compute_service import ComputeService

@chaifen.route('/compute/<int:fee>/<int:amount>')
def get_detail(fee=None,amount=None):
    results = ComputeService().compute(fee,amount)
    return "123"
