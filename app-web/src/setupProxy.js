const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function(app) {
  app.use(
    '/api',
    createProxyMiddleware({
      target: 'https://wklab094d7.execute-api.eu-west-1.amazonaws.com/items',
      changeOrigin: true,
    })
  );
};
 