import random
from flask import request
from flask import Flask

app = Flask(__name__)

@app.route('/random')
def getrandom():
    n = int(request.args.get('n', 10000))
    x = random.randint(0, n)
    return 'The random number in the range of [0..%d] is %d' % (n, x)

if __name__ == '__main__':
  # Enable Python Cloud Debugger if installed.
  try:
    import googleclouddebugger
    googleclouddebugger.AttachDebugger()
  except BaseException:
    pass

  app.run(host='0.0.0.0', port=8080)
