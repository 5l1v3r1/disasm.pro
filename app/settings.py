from flask import session
from  .constants import keystone_modes
from . import ninja_socketio
from keystone import *
import copy
from flask_socketio import emit


#This is basically the management of user's assembler/disassemblers config options

#New update from client
@ninja_socketio.on('update_settings')
def update(options):
    try:
        session['settings'] = copy.copy(options)
    except:
        return False

def get_settings():
    if 'settings' not in session:
        emit('get_settings')
        raise Exception("No settings initialized")
    return session['settings']

