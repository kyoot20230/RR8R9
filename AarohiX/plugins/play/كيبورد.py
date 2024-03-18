import pyrogram
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import OWNER_ID
from AarohiX import app

# تعريف الكيبورد المخصص للمطور
developer_keyboard = ReplyKeyboardMarkup([
	[('تفعيل التواصل'),('/broadcast'),('حاله التواصل')],
	[('ضع قناة الاشتراك'),('حذف قناه الاشتراك')],
	[('تفعيل الاشتراك'),('تعطيل الاشتراك'),('قناه الاشتراك')],
	[('حاله الاشتراك'),('الاحصائيات')],
	[('تفعيل اليوتيوب'),('تعطيل اليوتيوب'),('حاله اليوتيوب')],
	[('حذف الاعضاء الفيك'),('حذف الجروبات الفيك')],
	[('الاصدار'),('تحديث السورس'),('سرعه السيرفر')],
	[('اذاعه للمستخدمين'),('اذاعه للجروبات')],
	[('اذاعه للمطورين'),('اذاعه للاساسيين'),('اذاعه للقنوات')],
	[('اذاعه للكل'),('توجيه للكل')],
	[('توجيه للمستخدمين'),('توجيه للجروبات'),('توجيه للقنوات')],
	[('توجيه للاساسيين'),('توجيه للمطورين')],
	[('رفع مطور'),('تنزيل مطور'),('عرض المطورين')],
	[('رفع مطور اساسي'),('تنزيل مطور اساسي')],
	[('عرض الاساسيين'),('مسح الاساسيين'),('مسح المطورين')],
	[('نسخه احتياطيه اساسيه'),('نسخه احتياطيه 2')],
	[('حظر عضو'),('الغاء حظر عضو'),('عرض المحظورين')],
	[('تغيير مالك البوت'),('تغيير اسم البوت')],
	[('تفعيل البوت'),('تعطيل البوت'),('حاله البوت')],
	[('مسح المحظورين'),('تغيير داتابيس البوت')],
	[('اخفاء الكيبورد ⚒️')]],
	resize_keyboard=True,
)

# دالة للاستجابة عند استخدام المطور لأمر /start
@app.on_message(filters.command("start") & filters.user(OWNER_ID))
async def start_command(client, message):
    # إرسال لوحة المفاتيح المخصصة للمطور
    await message.reply("أهلا بك! اختر إحدى الخيارات:", reply_markup=developer_keyboard)

# دالة للرد على الرسائل الخاصة بالمطور
@app.on_message(filters.user(OWNER_ID) & filters.private & filters.text)
async def developer_message(client, message):
    # إرسال لوحة المفاتيح المخصصة للمطور
    await message.reply("أهلا بك! اختر إحدى الخيارات:", reply_markup=developer_keyboard)
