const http = require('http')
const url = require('url')

http.createServer(function (request, response) {
  var proxy = http.request({
    port: 80,
    hostname: request.headers['host'],
    method: request.method,
    url: url.parse(request.url),
    headers: request.headers
  })

  proxy.addListener('response', function (proxyResponse) {
    proxyResponse.addListener('data', function (chunk) {
      response.write(chunk, 'binary')
    })
    proxyResponse.addListener('end', function () {
      response.end()
    })
    response.writeHead(proxyResponse.statusCode, proxyResponse.headers)
  })

  request.addListener('data', function (chunk) {
    proxy.write(chunk, 'binary')
  })

  request.addListener('end', function () {
    proxy.end()
  })
}).listen(8080)
