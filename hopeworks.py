from math import pi, sin, cos
 
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3
from panda3d.core import CollisionTraverser,CollisionNode, CollisionSphere
from panda3d.core import CollisionHandlerQueue,CollisionRay, CollisionHandlerEvent
from panda3d.core import Vec3,Vec4,BitMask32
from direct.task.Task import Task
from math import pi, sin, cos
from pandac.PandaModules import loadPrcFileData
from direct.gui.OnscreenText import OnscreenText
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from panda3d.core import Filename,AmbientLight,DirectionalLight
from panda3d.core import PandaNode,NodePath,Camera,TextNode
from panda3d.core import Vec3,Vec4,BitMask32
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3
from direct.gui.OnscreenImage import OnscreenImage
from panda3d.core import TransparencyAttrib
import sys
from pandac.PandaModules import CollisionHandlerQueue, CollisionNode, CollisionSphere, CollisionTraverser
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3 

class MyApp(ShowBase):

  

    def __init__(self):
	global collide
        ShowBase.__init__(self)

	self.traverser = CollisionTraverser('traverser1')
	base.cTrav = self.traverser
	#traverser.addCollider(cnode1, handler)

	entry = 1

	imageObject = OnscreenImage(image = '/Users/devanshi/Downloads/sky.png', pos = (0, 0, 0), scale = 2)
	imageObject.setTransparency(TransparencyAttrib.MAlpha)
	base.cam.node().getDisplayRegion(0).setSort(20)
		
	self.forest=NodePath(PandaNode("Forest Root"))
        self.forest.reparentTo(render)
        loader.loadModel("models/background").reparentTo(self.forest)
        loader.loadModel("models/foliage01").reparentTo(self.forest)
        loader.loadModel("models/foliage02").reparentTo(self.forest)
        loader.loadModel("models/foliage03").reparentTo(self.forest)
        loader.loadModel("models/foliage04").reparentTo(self.forest)
        loader.loadModel("models/foliage05").reparentTo(self.forest)
        loader.loadModel("models/foliage06").reparentTo(self.forest)
        loader.loadModel("models/foliage07").reparentTo(self.forest)
        loader.loadModel("models/foliage08").reparentTo(self.forest)
        loader.loadModel("models/foliage09").reparentTo(self.forest)
	
	
	self.forest1=NodePath(PandaNode("Forest Root"))
        self.forest1.reparentTo(render)
        
        loader.loadModel("models/foliage01").reparentTo(self.forest1)
        loader.loadModel("models/foliage02").reparentTo(self.forest1)
        loader.loadModel("models/foliage03").reparentTo(self.forest1)
        loader.loadModel("models/foliage04").reparentTo(self.forest1)
        loader.loadModel("models/foliage05").reparentTo(self.forest1)
        loader.loadModel("models/foliage06").reparentTo(self.forest1)
        loader.loadModel("models/foliage07").reparentTo(self.forest1)
        loader.loadModel("models/foliage08").reparentTo(self.forest1)
        loader.loadModel("models/foliage09").reparentTo(self.forest1)

        self.forest.hide(BitMask32.bit(1))
	
        self.forest.setScale(2.5, 2.5, 2.5)
        self.forest.setPos(0, 0, -2)

        self.forest1.hide(BitMask32.bit(1))
	
        self.forest1.setScale(1.5, 1.5, 1.5)
        self.forest1.setPos(-1,-1, 0)

	self.forest2=NodePath(PandaNode("Forest Root"))
        self.forest2.reparentTo(render)
        
        loader.loadModel("models/foliage01").reparentTo(self.forest2)
        loader.loadModel("models/foliage02").reparentTo(self.forest2)
        loader.loadModel("models/foliage03").reparentTo(self.forest2)
        loader.loadModel("models/foliage04").reparentTo(self.forest2)
        loader.loadModel("models/foliage05").reparentTo(self.forest2)
        loader.loadModel("models/foliage06").reparentTo(self.forest2)
        loader.loadModel("models/foliage07").reparentTo(self.forest2)
        loader.loadModel("models/foliage08").reparentTo(self.forest2)
        loader.loadModel("models/foliage09").reparentTo(self.forest2)

        self.forest2.hide(BitMask32.bit(1))

        self.forest1.setScale(1.5, 1.5, 1.5)
        self.forest1.setPos(1,1, 0)

	self.stall = self.loader.loadModel("models/patch/cornfield")
	self.stall.reparentTo(self.render)
	self.stall.setScale(0.5)
	self.stall.setPos(40,0,1)
	self.stall.setHpr(0,0,0)
	self.tex1=self.loader.loadTexture("models/water.png")
	self.stall.setTexture(self.tex1,1)

	self.flock = Actor("models/goose/goosemodelonly",  {"gfly":"models/goose/gooseanimationonly"
                       })
        self.flock.setScale(0.05, 0.05, 0.05)
	self.flock.setPos(0,-30,13)
        self.flock.reparentTo(self.render)
	self.flock.loop("gfly")
	self.tex2=self.loader.loadTexture("models/orange.jpg")
	self.flock.setTexture(self.tex2,1)

	self.camera.setPos(0,0,0)
	self.camera.setHpr(90,0,0)

       # Create the four lerp intervals needed for the panda to
        # walk back and forth.
        pandaPosInterval1 = self.flock.posInterval(13,
                                                        Point3(-5, -30, 13),
                                                        startPos=Point3(5, -30, 13))
        pandaPosInterval2 = self.flock.posInterval(13,
                                                        Point3(5, -30, 13),
                                                        startPos=Point3(-5, -30, 13))
        pandaHprInterval1 = self.flock.hprInterval(3,
                                                        Point3(0, 0, 0),
                                                        startHpr=Point3(180, 0, 0))
        pandaHprInterval2 = self.flock.hprInterval(3,
                                                        Point3(180, 0, 0),
                                                        startHpr=Point3(0, 0, 0))
 
        # Create and play the sequence that coordinates the intervals.
        self.pandaPace = Sequence(pandaPosInterval1,
                                  pandaHprInterval1,
                                  pandaPosInterval2,
                                  pandaHprInterval2,
                                  name="pandaPace")
        self.pandaPace.loop()

		
	
	
        # Disable the camera trackball controls.
        #self.disableMouse()
 
        # Load the environment model.
        self.environ = self.loader.loadModel("models/environment1")
        # Reparent the model to render.
        self.environ.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.environ.setScale(0.25, 0.25, 0.25)
        self.environ.setPos(-8, 42, 0)

	self.boy =  Actor("models/trex/trex",  {"run":"models/trex/trex-run",
                                  "eat":"models/trex/trex-eat"})
	self.boy.reparentTo(self.render)
	self.boy.setPos(0,0,0)
	self.boy.setScale(0.5)
	self.isMoving = False
	self.myAnimControl = self.boy.getAnimControl('run')
				
	base.camera.setPos(self.boy.getX(),self.boy.getY()+10,20)
	self.floater = NodePath(PandaNode("floater"))
	self.floater.reparentTo(render)
		
	self.cBoy = self.boy.attachNewNode(CollisionNode('cBoyNode'))
	self.cBoy.node().addSolid(CollisionSphere(0, 0, 3, 8.5))
	#self.cBoy.show()
		
	#self.cPond = self.stall.attachNewNode(CollisionNode('cPond'))
	#self.cPond.node().addSolid(CollisionSphere(40, 0, 1, 70))
	#self.cPond.show()
	
 
        # Add the spinCameraTask procedure to the task manager.
        #self.taskMgr.add(self.spinCameraTask,"asdsad")
	self.keyMap = {"left":0, "right":0, "forward":0, "cam-left":0, "cam-right":0}

	cs1 = CollisionSphere(0, 0, 0, 2)
	self.cnodePath1 = render.attachNewNode(CollisionNode('cnode1'))
	self.cnodePath1.node().addSolid(cs1)
	#self.cnodePath1.setCollideMask(BitMask32(0x10))
	#self.cnodePath1.show()

	
	self.taskMgr.add(self.moveSphere1, "sfasdasf")
 

	cs2 = CollisionSphere(0, 0, 0, 1)
	self.cnodePath2 = render.attachNewNode(CollisionNode('cnode2'))
	self.cnodePath2.node().addSolid(cs2)
	#self.cnodePath2.reparentTo(self.render)
	#self.cnodePath2.node().setFromCollideMask(BitMask32.bit(0))
        #self.cnodePath2.node().setIntoCollideMask(BitMask32.allOff())
	#self.cnodePath2.show()

	self.taskMgr.add(self.moveSphere2, "sfasd")


	handler = CollisionHandlerEvent()
	handler.addInPattern('cnode1-into-cnode2')
	handler.addAgainPattern('cnode1-again-cnode2')
	handler.addOutPattern('cs1-out-cs2')


	self.accept('cnode1-into-cnode2', self.collide)
	#self.accept('cs1-out-cs2', self.collide)
	#self.accept('cnode1-again-cnode2', self.collide)


	self.traverser.addCollider(self.cnodePath1, handler)

        # Load and transform the panda actor.
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.005, 0.005, 0.005)
        self.pandaActor.reparentTo(self.render)
        # Loop its animation.
        self.pandaActor.loop("walk")

	self.taskMgr.add(self.movePanda, "Sasdas")
	
	self.pandaActor2 = Actor("models/panda-model",{"walk": "models/panda-walk4"})
        self.pandaActor2.setScale(0.003, 0.003, 0.003)
        self.pandaActor2.reparentTo(self.render)
        # Loop its animation.
        self.pandaActor2.loop("walk")

	self.taskMgr.add(self.movePanda2, "Sak")

	self.camera.setPos(0,0,0)
	self.camera.setHpr(90,0,0)

	self.cTrav1=CollisionTraverser()
	self.collisionHandler1 = CollisionHandlerQueue()
	self.cTrav1.addCollider(self.cBoy, self.collisionHandler1)

	self.taskMgr.add(self.boyMoveTask, "BoyMoveTask")
		
	#self.accept("v",self.switchView)
	self.accept("escape", sys.exit)
	self.accept("arrow_left", self.setKey, ["left",1])
	self.accept("arrow_right", self.setKey, ["right",1])
	self.accept("arrow_up", self.setKey, ["forward",1])
	#self.accept("a", self.setKey, ["cam-left",1])
	#self.accept("s", self.setKey, ["cam-right",1])
	self.accept("arrow_left-up", self.setKey, ["left",0])
	self.accept("arrow_right-up", self.setKey, ["right",0])
	self.accept("arrow_up-up", self.setKey, ["forward",0])
	#self.accept("a-up", self.setKey, ["cam-left",0])
	#self.accept("s-up", self.setKey, ["cam-right",0])

	self.cTrav2=CollisionTraverser()
	self.collisionHandler2 = CollisionHandlerQueue()
	self.cTrav2.addCollider(self.cBoy, self.collisionHandler2)
		
		
		

    # Define a procedure to move the camera.
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(0,0,50)
	self.camera.setHpr(0, -90, 0)
        return Task.cont

    def movePanda(self, task):
        angleDegrees = (task.time) * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.pandaActor.setPos(10 * sin(angleRadians), -10.0 * cos(angleRadians), 0)
        self.pandaActor.setHpr(90+angleDegrees, 0, 0)
        return Task.cont
	
    def movePanda2(self, task):
        angleDegrees = (task.time) * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.pandaActor2.setPos(10.0 * sin(angleRadians), 10.0 * cos(angleRadians), 0)
        self.pandaActor2.setHpr(-270-angleDegrees, 0, 0)
        return Task.cont

    def moveSphere2(self, task):
        angleDegrees = (task.time) * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.cnodePath2.setPos(10.0 * sin(angleRadians), 10.0 * cos(angleRadians), 1)
        self.cnodePath2.setHpr(90+angleDegrees, 0, 0)
        return Task.cont

    def moveSphere1(self, task):
        angleDegrees = (task.time) * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.cnodePath1.setPos(10 * sin(angleRadians), -10.0 * cos(angleRadians), 1)
        self.cnodePath1.setHpr(90+angleDegrees, 0, 0)
	return Task.cont

    def fly(self, task):
	angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
	x = self.pandaActor2.getX()
	y = self.pandaActor2.getY()
	p = self.pandaActor2.getH()
	self.pandaActor2.setPos(x, ((task.time)*(task.time))+20 * sin(angleRadians), 10.0 * sin(angleRadians))
	self.cnodePath2.setPos(x, ((task.time)*(task.time))+20 * sin(angleRadians), 10.0 * sin(angleRadians))
	self.pandaActor2.setHpr(p, -(angleDegrees*10), 0)
	return Task.cont

    def collide(self, entry):
	print "abc"
	#self.pandaActor2.setPos(0,0,2)
	self.taskMgr.remove("Sak")
	self.taskMgr.remove("sfasd")
	self.taskMgr.add(self.fly, "Sasopi")
	#self.pandaActor3 = Actor("models/panda-model",
        #               {"walk": "models/panda-walk4"})
       	#self.pandaActor3.setScale(0.005, 0.005, 0.005)
	#self.pandaActor3.setPos(0, 0, 1)
	#self.camera.setPos(0,0,50)


    def setKey(self, key, value):
		self.keyMap[key] = value
        

    def boyMoveTask(self, task):
		base.camera.reparentTo(self.boy)	
		base.camera.setPos(0,40,0)
		
		
		base.camera.lookAt(self.boy)
		if (self.keyMap["cam-left"]!=0):
			self.camera.setX(base.camera, -20 * globalClock.getDt())
		if (self.keyMap["cam-right"]!=0):
			self.camera.setX(base.camera, +20 * globalClock.getDt())

		self.startPos = self.boy.getPos()

		if (self.keyMap["left"]!=0):
			self.boy.setH(self.boy.getH() + 300 * globalClock.getDt())
		if (self.keyMap["right"]!=0):
			self.boy.setH(self.boy.getH() - 300 * globalClock.getDt())
		if (self.keyMap["forward"]!=0):
			self.boy.setY(self.boy, -35 * globalClock.getDt())

		if (self.keyMap["forward"]!=0) or (self.keyMap["left"]!=0) or (self.keyMap["right"]!=0):
			if self.isMoving is False:
				self.boy.loop("run")
				self.isMoving = True
		else:
			if self.isMoving:
				self.boy.stop()
				self.boy.pose("walk",5)
				self.isMoving = False

		camvec = self.boy.getPos() - base.camera.getPos()
		camvec.setZ(20)
		camdist = camvec.length()
		camvec.normalize()
		if (camdist > 50):
			base.camera.setPos(base.camera.getPos() + camvec*(camdist-50))
			camdist = 50.0
		if (camdist < 25.0):
			base.camera.setPos(base.camera.getPos() - camvec*(25-camdist))
			camdist = 25.0
		
		self.cTrav1.traverse(render)
		self.collisionHandler1.sortEntries()
		if self.collisionHandler1.getNumEntries() == 0:
			self.startPos = self.boy.getPos()
			#self.boy.loop("eat")
		else:
			self.boy.setPos(self.startPos);
			
			#print self.collisionHandler1.getEntry(0)
		

		base.camera.setZ(self.boy.getZ() + 10)
		return Task.again


app = MyApp()
app.run()