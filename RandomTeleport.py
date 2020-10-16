# -*- encoding: utf-8 -*-
"""
File : RandomTeleport.py
-----------------------------------------------------------
Copyright © 2020 | Enaium | All rights reserved.
"""
import random
import cn.nukkit.level.Position as pos

manager.createCommand("rtp", u"随机传送", "rtp")


def rtp(sender, args):
    sender.teleport(pos.fromObject(manager.buildvec3(random.randint(-999999, 999999), 90, random.randint(-999999, 999999)), sender.getLevel()))
