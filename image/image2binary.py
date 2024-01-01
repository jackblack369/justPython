import base64
from PIL import Image

from sqlmodel import SQLModel, Field, create_engine, Session
from sqlalchemy import BINARY, Column


class test_icon(SQLModel, table=True):
    id: int = Field(primary_key=True)
    icon_binary: bytes = Field(sa_column=Column(BINARY, nullable=False))


#image_path = "/Users/dongwei/Pictures/wallpapers/will.jpg"
image_path = "/Users/dongwei/Pictures/logo/logo_head.png"
image = Image.open(image_path)


image_binary = image.tobytes()
base64_string = base64.b64encode(image_binary).decode('utf-8')
print(f"base64_string: {base64_string}")


# 创建数据库引擎
engine = create_engine("mysql+pymysql://root:123123@172:3307/dongwei")

# 创建会话
session = Session(engine)

# 创建 User 对象并设置属性值
user = test_icon(id=1, icon_binary=image_binary)

# 添加 User 对象到会话中
session.add(user)

# 提交事务
session.commit()