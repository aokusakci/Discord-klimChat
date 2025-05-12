import discord
from discord.ext import commands
import os, random
import requests
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)



@bot.command()
async def cevre(ctx, *, message_content):
    if message_content.startswith("plastiği doğada nasıl daha hızlı yok edebileceğimi biliyor musun?"):
        await ctx.send(
            "Plastiği doğada daha hızlı yok etmek için biyolojik olarak parçalanabilen plastikler kullanabilirsiniz. "
            "Ayrıca, plastik atıkları geri dönüşüm kutularına atarak yeniden kullanılabilir ürünlere dönüştürülmesini sağlayabilirsiniz. "
            "Bunun dışında *Ideonella sakaiensis* bakterisi, PET plastikleri parçalayabilen bir bakteri türüdür."
        )
    elif message_content.startswith("metali doğada nasıl daha hızlı yok edebileceğimi biliyor musun?"):
        await ctx.send(
            "Metalleri doğada daha hızlı yok etmek için geri dönüşüm tesislerine göndererek eritilip yeniden kullanılmasını sağlayabilirsiniz. "
            "Ayrıca, *Acidithiobacillus ferrooxidans* ve *Leptospirillum ferrooxidans* gibi bakteriler metal yüzeyleri oksitleyerek parçalayabilir."
        )
    elif message_content.startswith("camı doğada nasıl daha hızlı yok edebileceğimi biliyor musun?"):
        await ctx.send(
            "Cam doğada mikroorganizmalar tarafından kolayca parçalanamaz. Ancak geri dönüşüm kutularına atarak yeniden cam ürünlere dönüştürülmesini sağlayabilirsiniz. "
            "Cam atıkları sanat projelerinde veya dekoratif amaçlarla yeniden kullanabilirsiniz."
        )
    elif message_content.startswith("kağıdı doğada nasıl daha hızlı yok edebileceğimi biliyor musun?"):
        await ctx.send(
            "Kağıdı doğada daha hızlı yok etmek için geri dönüşüm kutularına atarak yeniden kağıt ürünlere dönüştürülmesini sağlayabilirsiniz. "
            "Ayrıca, *Trichoderma reesei* gibi mantarlar selülozu parçalayarak kağıt atıklarını ayrıştırabilir."
        )
    elif message_content.startswith("ahşabı doğada nasıl daha hızlı yok edebileceğimi biliyor musun?"):
        await ctx.send(
            "Ahşabı doğada daha hızlı yok etmek için *Phanerochaete chrysosporium* gibi beyaz çürüklük mantarları kullanılabilir. "
            "Ayrıca, eski mobilyaları tamir ederek veya boyayarak yeniden kullanabilirsiniz."
        )
    elif message_content.startswith("betonu doğada nasıl daha hızlı yok edebileceğimi biliyor musun?"):
        await ctx.send(
            "Beton doğada mikroorganizmalarla kolayca yok edilemez. Ancak geri dönüşüm tesislerinde kırılarak yol yapımında dolgu malzemesi olarak kullanılabilir."
        )
    elif message_content.startswith("işlenmiş demiri doğada nasıl daha hızlı yok edebileceğimi biliyor musun?"):
        await ctx.send(
            "İşlenmiş demiri doğada daha hızlı yok etmek için *Gallionella ferruginea* gibi demir oksitleyen bakteriler kullanılabilir. "
            "Ayrıca, hurda metal toplayıcılarına teslim ederek geri dönüşüm sürecine dahil edebilirsiniz."
        )
    elif message_content.startswith("işlenmemiş demiri doğada nasıl daha hızlı yok edebileceğimi biliyor musun?"):
        await ctx.send(
            "İşlenmemiş demiri doğada daha hızlı yok etmek için *Acidithiobacillus ferrooxidans* gibi bakteriler kullanılabilir. "
            "Ayrıca, demir atıkları inşaat projelerinde dolgu malzemesi olarak değerlendirilebilir."
        )
    elif message_content.startswith("çeliği doğada nasıl daha hızlı yok edebileceğimi biliyor musun?"):
        await ctx.send(
            "Çeliği doğada daha hızlı yok etmek için demir oksitleyen bakteriler, örneğin *Leptospirillum ferrooxidans*, kullanılabilir. "
            "Ayrıca, eski çelik ürünleri tamir ederek yeniden kullanabilirsiniz."
        )
    elif message_content.startswith("alüminyumu doğada nasıl daha hızlı yok edebileceğimi biliyor musun?"):
        await ctx.send(
            "Alüminyumu doğada daha hızlı yok etmek için *Pseudomonas aeruginosa* gibi bakteriler kullanılabilir. "
            "Ayrıca, alüminyum kutuları geri dönüşüm kutularına atarak yeniden kullanılabilir ürünlere dönüştürebilirsiniz."
        )
    elif message_content.startswith("kurşunu doğada nasıl daha hızlı yok edebileceğimi biliyor musun?"):
        await ctx.send(
            "Kurşunu doğada daha hızlı yok etmek için *Desulfovibrio desulfuricans* gibi sülfat indirgeyen bakteriler kullanılabilir. "
            "Eski piller ve aküleri geri dönüşüm tesislerine teslim etmek önemlidir."
        )
    elif message_content.startswith("çinkoyu doğada nasıl daha hızlı yok edebileceğimi biliyor musun?"):
        await ctx.send(
            "Çinkoyu doğada daha hızlı yok etmek için *Acidithiobacillus thiooxidans* gibi bakteriler kullanılabilir. "
            "Ayrıca, çinko içeren ürünleri doğru şekilde ayrıştırarak geri dönüşüme kazandırabilirsiniz."
        )
    elif message_content.startswith("altını doğada nasıl daha hızlı yok edebileceğimi biliyor musun?"):
        await ctx.send(
            "Altını doğada mikroorganizmalarla yok etmek zordur. Ancak altın içeren elektronik atıkları geri dönüşüm tesislerine göndererek altının geri kazanılmasını sağlayabilirsiniz."
        )
    elif message_content.startswith("gümüşü doğada nasıl daha hızlı yok edebileceğimi biliyor musun?"):
        await ctx.send(
            "Gümüşü doğada daha hızlı yok etmek için *Pseudomonas stutzeri* gibi bakteriler kullanılabilir. "
            "Eski gümüş takıları eriterek yeni takılar yapılmasını sağlayabilirsiniz."
        )
    elif message_content.startswith("kalayı doğada nasıl daha hızlı yok edebileceğimi biliyor musun?"):
        await ctx.send(
            "Kalayı doğada daha hızlı yok etmek için kalay oksitleyen mikroorganizmalar araştırılabilir. "
            "Ayrıca, kalay kaplama ürünleri tamir ederek ömürlerini uzatabilirsiniz."
        )
    elif message_content.startswith("nikelin doğada nasıl daha hızlı yok edebileceğimi biliyor musun?"):
        await ctx.send(
            "Nikeli doğada daha hızlı yok etmek için *Acidithiobacillus ferrooxidans* gibi bakteriler kullanılabilir. "
            "Ayrıca, nikel içeren pillerin geri dönüşümünü sağlamak önemlidir."
        )
    elif message_content.startswith("titaniumun doğada nasıl daha hızlı yok edebileceğimi biliyor musun?"):
        await ctx.send(
            "Titanyumu doğada mikroorganizmalarla yok etmek zordur. Ancak geri dönüşüm tesislerine göndererek yeniden kullanılmasını sağlayabilirsiniz."
        )
    elif message_content.startswith("kobaltın doğada nasıl daha hızlı yok edebileceğimi biliyor musun?"):
        await ctx.send(
            "Kobaltı doğada daha hızlı yok etmek için *Acidithiobacillus ferrooxidans* gibi bakteriler kullanılabilir. "
            "Ayrıca, kobalt içeren pillerin geri dönüşümünü sağlamak önemlidir."
        )
    elif message_content.startswith("manganesin doğada nasıl daha hızlı yok edebileceğimi biliyor musun?"):
        await ctx.send(
            "Manganezi doğada daha hızlı yok etmek için *Leptothrix discophora* gibi bakteriler kullanılabilir. "
            "Ayrıca, manganez içeren ürünleri geri dönüşüm tesislerine gönderebilirsiniz."
        )
    elif message_content.startswith("fosforun doğada nasıl daha hızlı yok edebileceğimi biliyor musun?"):
        await ctx.send(
            "Fosforu doğada daha hızlı yok etmek için fosfat çözücü bakteriler, örneğin *Bacillus megaterium*, kullanılabilir. "
            "Ayrıca, fosfor içeren gübre atıklarını geri dönüşüm tesislerine gönderebilirsiniz."
        )
    elif message_content.startswith("kükürtün doğada nasıl daha hızlı yok edebileceğimi biliyor musun?"):
        await ctx.send(
            "Kükürtü doğada daha hızlı yok etmek için *Thiobacillus thiooxidans* gibi bakteriler kullanılabilir. "
            "Ayrıca, kükürt içeren ürünleri tarımda gübre olarak değerlendirebilirsiniz."
        )
    elif message_content.startswith("sodyumun doğada nasıl daha hızlı yok edebileceğimi biliyor musun?"):
        await ctx.send(
            "Sodyumu doğada mikroorganizmalarla yok etmek zordur. Ancak geri dönüşüm tesislerine göndererek yeniden kullanılmasını sağlayabilirsiniz."
        )
# ...existing code...

