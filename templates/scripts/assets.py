#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from webassets import Environment, Bundle

dir_static = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'static')

static_env = Environment(dir_static)

static_env.register('js_all', Bundle(
    'js/script.js',
    output='gen/all.js'))
static_env['js_all'].build()

# font-awesome is broken when included
static_env.register('css_all', Bundle(
    'css/style.css',
    filters='cssmin', output='gen/all.css'))
static_env['css_all'].build()