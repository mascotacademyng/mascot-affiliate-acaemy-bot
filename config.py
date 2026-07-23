import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Telegram Bot Token
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Coach Information
COACH_NAME = "Coach Mascot"
COACH_USERNAME = "@mascotaffiliate"

# Contact Links
WHATSAPP_LINK = "https://wa.me/qr/5VFO46UL6FWPI1"
TELEGRAM_CHANNEL = "https://t.me/macotdigitalacademy"

# Premium Training
SELAR_LINK = "https://selar.com/p8v1233911"
PREMIUM_PRICE = "₦1,500"

# Bot Information
BOT_NAME = "Mascot Affiliate Academy"
BOT_USERNAME = "@mascotaffiliatebot"

# Certificate
CERTIFICATE_TITLE = "Affiliate Marketing Mastery for Beginners"

# Database
DATABASE_NAME = "users.db"
