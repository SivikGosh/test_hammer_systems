const csrftoken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

export const AppConfig = {
    csrftoken: csrftoken,
    apiUrl: 'http://localhost:8000',
    phoneRegex: /^\+?[1-9]\d{9,14}$/,
    codeRegex: /^\d{4}$/,
    activateCodeRegex: /^(\d{6}|\w{6})$/,
    codeTTL: 300,
};
