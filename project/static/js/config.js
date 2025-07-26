export const AppConfig = {
    csrftoken: document.querySelector('meta[name="csrf-token"]').getAttribute('content'),
    apiUrl: document.querySelector('meta[name="site-url"]').getAttribute('content'),
    phoneRegex: /^\+?[1-9]\d{9,14}$/,
    codeRegex: /^\d{4}$/,
    activateCodeRegex: /^(\d{6}|\w{6})$/,
    codeTTL: 300,
};
