import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
import os
from dotenv import load_dotenv
load_dotenv()

# configuration       
cloudinary.config( 
    cloud_name = "dzddmjqwi", 
    api_key = "187948155668464", 
    api_secret = os.environ.get("CLOUDINARY_API_SECRET"), # Click 'View API Keys' above to copy your API secret
    secure=True
)

images = ["C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0010-IMG_20210301_141832.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0011-IMG_20221103_125418.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0011.1-IMG_20221211_092349.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0011.2-IMG_20230106_131827.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0012-IMG_20210316_115323.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0013IMG_20210211_100738.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0014IMG_20210212_145803.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0015-IMG_20221129_012018.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0015IMG_20210910_094904.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0017.1-IMG_20221122_101616.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0018.2-IMG_20221209_133654.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0019-IMG_20210124_174501.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0020-IMG_20200617_210057.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0027-IMG_20210221_153525.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0028-IMG_20210520_164739.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0029-IMG_20210313_121007.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0030.1-IMG_20221215_132717.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0031-IMG_20210803_171009.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0031.0.1PXL_20230323_093355886.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0031.1PXL_20230322_174300404.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0032-IMG_20230111_094942.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0032.1PXL_20230609_115608065.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0032.2PXL_20230622_093139774.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0033-IMG_20210116_140512.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0034-IMG_20210430_094432.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0035-20190327_122555.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0036-20190326_113258.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0037-IMG_20200702_152837.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0038-IMG_20210617_092732.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0039-IMG_20220513_170236.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/004-IMG_20210911_130603.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/004.1-IMG_20221221_133015.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0040-IMG_20210220_143120.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0041-20190419_123042.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0046-IMG_20210218_212801.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0046.01-PXL_20230301_103045870.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0046.02PXL_20230523_095853080.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0047-IMG_20210220_235622.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0048-IMG_20220924_120139.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0048.1-IMG_20191126_214115.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/005-20190427_171927.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0054-IMG_20221201_125121.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0054.0.5-PXL_20230304_203052506.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0054.01-PXL_20230309_102213244.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0055-IMG_20210706_125139.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0056-IMG_20210930_155410.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/006-IMG_20211214_143339-2.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/006.1-IMG_20221013_161819.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0061.2-IMG_20221122_162551.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0068-20190219_103847.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0069-20190407_093022.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0069.1-IMG_20210627_235741.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/007-IMG_20221121_153615.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/008-IMG_20210218_211713.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/008.0.5PXL_20230413_113917709.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0080-IMG_20210309_112351.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0081-IMG_20200120_100654.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0082-20190411_151344.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0082.0.5PXL_20230821_103238980.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0083-IMG_20210913_111703.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0083.1-20190423_132513.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0083.1.05.PXL_20230402_110604460.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0083.2-IMG_20200426_132829-2.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0084-IMG_20210305_132933.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0085.1-IMG_20210306_145419.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0086-IMG_20210307_171016.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0086.1IMG_20221125_211146.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0087-20190407_093117-2.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0087.01-PXL_20230222_094339589.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0088.1-IMG_20221003_122413.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0089-IMG_20221121_120918-2.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0089.1-IMG_20221215_110803.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0089.120190411_150905.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/009.PXL_20230919_101318054.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0090.0PXL_20230401_152259332.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0090.1-IMG_20220607_120924.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0090.2PXL_20230913_120510305.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0091-IMG_20210615_195307.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0092.PXL_20230717_164452905.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0093-IMG_20221026_133149.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0093.0.3PXL_20230519_142441231.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0093.0.4-PXL_20230215_131332935-2.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0093.1IMG_20221129_151116.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0095.1-IMG_20221209_170225.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0096-PXL_20230311_110915890.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0096.1PXL_20230331_154553499.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0096.2PXL_20230331_175657106.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0097-IMG_20211014_093913.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0102.3-IMG_20221129_151025.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0102.4-IMG_20221130_142246.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0102.5-IMG_20230105_132642.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0102.6PXL_20230417_102015448.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0103.1PXL_20230912_083327025-2.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0103.8PXL_20230327_082009627.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0104-IMG_20210525_091109.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0105-IMG_20210525_091104.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0108.2-IMG_20210730_174227.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/0109-MVIMG_20200501_162343.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/090.3PXL_20230526_090906408.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/098.PXL_20230316_091128250.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/PXL_20230322_125043776.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/PXL_20230329_194741525.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/PXL_20230418_065326962.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/PXL_20230708_082552357.jpg",
        "C://Users/SamVerhezen/Desktop/gallerymarie/images/under_your_feet/PXL_20230711_122320285.jpg"
        ]

for image in images:

    # upload images
    image_link = image
    image_id = image.split("/")[-1].replace(".jpg", "")
    upload_result = cloudinary.uploader.upload(image_link,
                                                public_id=image_id,
                                                folder="under_your_feet")
    print(upload_result["secure_url"])

    # optimize delivery by resizing and applying auto-format and auto-quality
    optimize_url, _ = cloudinary_url("shoes", fetch_format="auto", quality="auto")
    print(optimize_url)

    # transform the image: auto-crop to square aspect_ratio
    # auto_crop_url, _ = cloudinary_url("shoes", width=500, height=500, crop="auto", gravity="auto")
    # print(auto_crop_url)