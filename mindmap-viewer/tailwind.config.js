/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        ember: {
          50: "#fdf7f2",
          100: "#fae8d7",
          200: "#f3c99f",
          300: "#eca969",
          400: "#e48a36",
          500: "#cb6f1c",
          600: "#9f5314",
          700: "#733a0f",
          800: "#47230a",
          900: "#1d0d03"
        }
      }
    }
  },
  plugins: []
};
