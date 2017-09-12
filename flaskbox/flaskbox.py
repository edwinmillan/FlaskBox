from flask import Flask, render_template, flash, redirect
from forms import *


app = Flask(__name__)
app.config.from_object(__name__)
app.config.update({
    'WTF_CSRF_ENABLED': True,
    'SECRET_KEY': 'super-secret-change-me-you-knob'
})


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title="Index")


@app.route('/tools')
def tools():
    return render_template('tools.html',
                           title="Tools")


@app.route('/tools/dns', methods=['GET', 'POST'])
def dns_lookup():
    form = DnsLookupForm()
    if form.validate_on_submit():
        flash(f'DNS Lookup for Hostname {form.hostname.data}')
        return redirect('/tools')
    return render_template('dns_lookup.html',
                           title='Dns Lookup',
                           form=form)


def main():
    app.run(host='0.0.0.0', debug=True)


if __name__ == '__main__':
    main()
