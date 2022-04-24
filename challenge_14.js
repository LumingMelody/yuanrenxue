CryptoJS = require('crypto-js')


window = this;

// (function anonymous(
// ) {
// window.s = window.a(window.t + '|' + window.num);window.a = window.s;
// })

function get_uc(num) {
    window.num = num;
    window.k = 'wdf2ff*TG@*(F4)*YH)g430HWR(*)' + 'wse';
    window.t = Date.parse(new Date())/1000;
    window.m = CryptoJS.enc.Utf8.parse(window.k);
        window.a = function(word){
            var srcs = CryptoJS.enc.Utf8.parse(word);
            var encrypted = CryptoJS.AES.encrypt(srcs, window.m, {
                mode: CryptoJS.mode.ECB,
                padding: CryptoJS.pad.Pkcs7
            });
            return encrypted.toString();
            };
    window.s = window.a(window.t + '|' + window.num);
    return window.s
}

// console.log(get_uc(2))
