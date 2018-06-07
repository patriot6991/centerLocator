import maya.cmds as mc

x = 0
y = 0
z = 0

for i in mc.ls(sl=True, fl=True):
    get_info = mc.pointPosition(i)
    x += get_info[0]
    y += get_info[1]
    z += get_info[2]

hoge = len(mc.ls(sl=True, fl=True))
x /= hoge
y /= hoge
z /= hoge

mc.spaceLocator()
mc.setAttr('%s.translateX' % (mc.ls(sl=True)[0]), x)
mc.setAttr('%s.translateY' % (mc.ls(sl=True)[0]), y)
mc.setAttr('%s.translateZ' % (mc.ls(sl=True)[0]), z)