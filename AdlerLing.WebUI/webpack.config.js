var path = require('path');
var HtmlWebPackPlugin = require('html-webpack-plugin');

module.exports = {
    entry: './src/index.js',
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'index_bundle.js'
    },
    module: {
        rules: [
            { test: /\.(js)$/, use: 'babel-loader' },
            { test: /\.(css)$/, use: ['style-loader', 'css-loader'] },
        ]
    },
    
    devServer: {
        historyApiFallback: true,
    },
    
    mode: 'development',

    plugins: [
        new HtmlWebPackPlugin({
            template: 'public/index.html'
        })
    ]
}