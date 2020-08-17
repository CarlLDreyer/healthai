module.exports = {
  css: {
    loaderOptions: {
      sass: {
        data: `
          @import "@/assets/styles/_variables.scss";
          $isProd: ${ process.env.NODE_ENV === 'production' };
        `
      }
    }
  },
  devServer: {
    // https: true,
    proxy: {
      '/webhooks/rest/webhook': {
        target: 'http://localhost:5005',
        secure: false
      }
    }
  }
}
