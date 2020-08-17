module.exports = {
  root: true,

  env: {
    node: true
  },

  'extends': [
    'plugin:vue/essential',
    '@vue/standard'
    // "plugin:vue/strongly-recommended"
  ],

  rules: {
    // 'no-console': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    // 'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    'comma-dangle': ['error', 'only-multiline'],
    'spaced-comment': 0,
    'no-return-assign': 0,
    'brace-style': [2, 'stroustrup', { 'allowSingleLine': true }],
    'no-unused-expressions': 0,
    // new
    'no-sequences': 0,
    'no-inner-declarations': 0,
    'vue/max-attributes-per-line': 0, // false?
    'template-curly-spacing': ['error', 'always'],
    'vue/no-parsing-error': [2, { 'x-invalid-end-tag': false }],
  },

  parserOptions: {
    parser: 'babel-eslint'
  },

}
