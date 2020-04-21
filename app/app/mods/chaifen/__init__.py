# coding=utf-8

from flask import Blueprint,request,session

chaifen = Blueprint('chaifen', __name__)

from . import views