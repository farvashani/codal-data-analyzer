#!/bin/bash
# 🚀 راه‌اندازی پروژه تحلیلگر کدال ایران
# Setup script for Codal Data Analyzer

echo "🚀 راه‌اندازی پروژه تحلیلگر کدال ایران"
echo "========================================"

# بررسی وجود Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 نصب نیست. لطفاً ابتدا Python3 را نصب کنید."
    exit 1
fi

echo "✅ Python3 موجود است: $(python3 --version)"

# ایجاد محیط مجازی
if [ ! -d "codal_env" ]; then
    echo "📦 ایجاد محیط مجازی..."
    python3 -m venv codal_env
    echo "✅ محیط مجازی ایجاد شد"
else
    echo "✅ محیط مجازی موجود است"
fi

# فعال‌سازی محیط مجازی
echo "🔧 فعال‌سازی محیط مجازی..."
source codal_env/bin/activate

# نصب کتابخانه‌ها
echo "📚 نصب کتابخانه‌های مورد نیاز..."
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "🎉 راه‌اندازی کامل شد!"
echo ""
echo "📋 دستورات مفید:"
echo "  فعال‌سازی محیط: source codal_env/bin/activate"
echo "  اجرای تست:      python test_codal.py"
echo "  اجرای تحلیلگر:  python codal_data_analyzer.py"
echo "  نوت‌بوک:        jupyter notebook codal_analysis.ipynb"
echo ""
echo "💡 برای شروع کار:"
echo "  1. source codal_env/bin/activate"
echo "  2. python test_codal.py"
echo ""
