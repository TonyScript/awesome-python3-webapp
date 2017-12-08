import orm, asyncio
from models import User, Blog, Comment

async def test(loop, **kw):
    await orm.create_pool(loop=loop, user='www-data', password='www-data', database='awesome')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    await u.save()
    await orm.destory_pool()


data=dict(name='gaf', email='235123345@qq.com', passwd='1312345', image='about:blank')
loop=asyncio.get_event_loop()
loop.run_until_complete(test(loop,**data))
loop.close()