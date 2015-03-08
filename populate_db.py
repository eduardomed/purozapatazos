from database import db_session, init_db
from models import Zapatazo


### This file is for testing purposes ###

init_db()

p_urls = [
		'https://s-media-cache-ak0.pinimg.com/236x/a3/3d/a6/a33da66e98c38438b07621c0b08780e2.jpg',
		'https://s-media-cache-ak0.pinimg.com/236x/d1/89/52/d18952c7ecfd1e1c983e2c12b201c9c6.jpg',
		'https://s-media-cache-ak0.pinimg.com/236x/0a/1e/35/0a1e350ad2481fb74dc9def31c4ce542.jpg',
		'https://s-media-cache-ak0.pinimg.com/236x/26/b4/21/26b421260b2e33b30618883311a16ab2.jpg',
		'https://s-media-cache-ak0.pinimg.com/236x/22/db/3f/22db3fe396a759c97f28ac09aef57a7b.jpg',
		'https://s-media-cache-ak0.pinimg.com/236x/27/83/03/2783032dcd2f56b9e6985c05c5c620fb.jpg',
		'https://s-media-cache-ak0.pinimg.com/236x/2b/85/55/2b8555515dcff59bb8fed40acd9c5bbe.jpg',
		'https://s-media-cache-ak0.pinimg.com/236x/fa/29/ab/fa29ab34b8a12fbe5a37be2a163ddd00.jpg',
		'https://s-media-cache-ak0.pinimg.com/236x/8e/f4/bb/8ef4bbadf94db867f5058e4f8d844b27.jpg',
		'https://s-media-cache-ak0.pinimg.com/236x/9c/95/cc/9c95cce84432c774af71ecc6fa382e31.jpg',
		'https://s-media-cache-ak0.pinimg.com/236x/ed/31/30/ed3130cb5d8d917fea070f4afed38749.jpg',
		'https://s-media-cache-ak0.pinimg.com/236x/c7/32/82/c73282ed6632cf4a168ad19dbb4e97ea.jpg',
		'https://s-media-cache-ak0.pinimg.com/236x/e1/11/e0/e111e0964001290eed30963fdf62d36a.jpg',
		'https://s-media-cache-ak0.pinimg.com/236x/5a/8b/56/5a8b569ae71b78a9d2b415a31b87f016.jpg',
		'https://s-media-cache-ak0.pinimg.com/236x/7d/07/f2/7d07f2b8ae41be9cccadfb1c7a8f78d5.jpg',
		'https://s-media-cache-ak0.pinimg.com/236x/c7/c8/fb/c7c8fbfae91b4812236758ccc35a5662.jpg',
		'https://s-media-cache-ak0.pinimg.com/236x/b4/84/23/b484230525f65514600dc0a0b050560b.jpg',
		'https://s-media-cache-ak0.pinimg.com/236x/e2/54/94/e254942b4a6ab262c2eb718db1a99fae.jpg',
		'https://s-media-cache-ak0.pinimg.com/236x/2b/b5/00/2bb500446827591d0a0d2cdc0e87d35c.jpg',
		'https://s-media-cache-ak0.pinimg.com/236x/56/0f/5a/560f5a91f92c140ccc5ff8243aa1123e.jpg',
		'https://s-media-cache-ak0.pinimg.com/236x/f0/3e/57/f03e577b2a5cd23dd8d0742e15650f07.jpg',
		'https://s-media-cache-ak0.pinimg.com/236x/f6/29/43/f629430c8308ad5a423cca492d313cf9.jpg',
		'https://s-media-cache-ak0.pinimg.com/236x/f5/04/e4/f504e4bd8889a29ab940d2ce0e2243b4.jpg',
		'https://s-media-cache-ak0.pinimg.com/236x/a0/df/a6/a0dfa6610b1dca6365087bcd859f06cc.jpg',
		'https://s-media-cache-ak0.pinimg.com/236x/24/f0/29/24f02965ae7061a71747a7a0522f15c9.jpg',]

for i in p_urls:
	z = Zapatazo(imglink = i)
	db_session.add(z)

db_session.commit()


### SQL, just place holder ###

# INSERT INTO zapatazos VALUES(1,'Zapatazo 1','static/images/zapatazo.jpg');
# INSERT INTO zapatazos VALUES(2,'Zapatazo 2','static/images/zapatazo.jpg');
# INSERT INTO zapatazos VALUES(3,'Zapatazo 3','static/images/zapatazo.jpg');


# CREATE TABLE zapatazos (
# 	id serial PRIMARY KEY, 
# 	imglink text not null
# );








