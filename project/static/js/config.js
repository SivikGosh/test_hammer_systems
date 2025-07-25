export const AppConfig = {
    csrftoken: '{{ csrf_token }}',
    apiUrl: 'http://localhost:8000',
    phoneRegex: /^\+?[1-9]\d{9,14}$/,
    codeRegex: /^\d{4}$/,
    codeTTL: 300,
};