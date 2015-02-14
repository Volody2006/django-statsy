
Django Statsy
========

[![Build Status](https://travis-ci.org/fata1ex/django-statsy.svg)](https://travis-ci.org/fata1ex/django-statsy) [![Coverage Status](https://coveralls.io/repos/fata1ex/django-statsy/badge.svg)](https://coveralls.io/r/fata1ex/django-statsy) [![Requirements Status](https://requires.io/github/fata1ex/django-statsy/requirements.svg?branch=master)](https://requires.io/github/fata1ex/django-statsy/requirements/?branch=master) [![PyPI version](https://badge.fury.io/py/django-statsy.svg)](http://badge.fury.io/py/django-statsy)

[![Stories in Ready](https://badge.waffle.io/fata1ex/django-statsy.svg?label=in%20progress&title=In%20Progress)](https://waffle.io/fata1ex/django-statsy)

Statsy is an application for collecting and displaying statistics in your Django project.


### Basic Usage

View decorator:

```python
@statsy.watch
def index(request):
    ...
```

```python
@statsy.watch(group='index', event='page_view')
def index(request):
    ...
```

Inside the view:

```python
def like(request):
  ...

  statsy.send(
    group='post', event='like', user=request.user,
    value=17, related_object=post
  )

  ...
```

CBV Mixin:

```python
class AboutView(WatchMixin, TemplateView):
    template_name = 'example/about.html'

    watch_group = 'info'
    watch_event = 'page_view'
```

From the template:

```javascript
{% load statsy %}

{% statsy %}

...

var statsy = new Statsy()

statsy.send({
  'group': 'post',
  'event': 'subscription'
});
```

### Installation

```
pip install django-statsy
```

```python
# settings.py

INSTALLED_APPS = (
  ...

  'statsy',
)
```

If you want to display collected statistics you will also have to add Statsy's URLs to your project's URLs.

```python
# urls.py
  ...

  url(r'^stats/', include('statsy.urls')),
  ...
```

### Collect Options

All are optional.
```python
# categorizing options
'group'
'event'

# some additional info about the stats object
'label'

# user associated with the action
# collected by default in @watch
'user'

# object of the action
'related_object'

# value can be <int>, <float> or <str>/<unicode>/etc.
'value'

# where did it happen
# collected by default in @watch
'url'

# how long did it take <int>
# collected by default in @watch
'duration'

# JSON for an extra data
'extra'
```

### Roadmap
- Enhanced statistics view
- Aggregation over time
- User tracking
- Realtime statistics

### License
[MIT](https://github.com/fata1ex/django-statsy/raw/master/LICENSE)
