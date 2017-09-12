from flask import Flask, render_template, flash, redirect
from forms import *
import dns
import geoip


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
    form = HostLookupForm()
    if form.validate_on_submit():
        lookup_info = dns.lookup(form.host.data)
        flash(f'DNS Lookup for Host {form.host.data} is: {lookup_info}')
        return redirect('/tools')
    return render_template('host_lookup.html',
                           title='Dns Lookup',
                           intent='DNS',
                           form=form)


@app.route('/tools/geoip', methods=['GET', 'POST'])
def geoip_lookup():
    form = HostLookupForm()
    if form.validate_on_submit():
        lookup_info = geoip.lookup(form.host.data)
        flash(f'DNS Lookup for Host {form.host.data} is: {lookup_info}')
        return redirect('/tools')
    return render_template('host_lookup.html',
                           title='Geoip Lookup',
                           intent='Geoip',
                           form=form)


def main():
    app.run(host='0.0.0.0', debug=True)


if __name__ == '__main__':
    main()
