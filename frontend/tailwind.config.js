/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        background: '#fdfdfd', // 极简纯净白
        sidebar: 'rgba(255, 255, 255, 0.7)',
        accent: '#4f46e5', // 优雅的靛蓝色
        textMain: '#1e293b', // 深灰蓝，代替纯黑
        textMuted: '#64748b'
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
      }
    },
  },
  plugins: [],
}
