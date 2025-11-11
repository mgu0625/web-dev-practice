import * as THREE from 'three'
import Experience from '../Experience.js'
import Environment from './Environment.js'
import Floor from './Floor.js'
import Fox from './Fox.js'

export default class World
{
    constructor()
    {
        this.experience = new Experience()
        // console.log('The World!')

        this.scene = this.experience.scene
        // console.log(this.scene)

        this.resources = this.experience.resources

        // console.log(this.resources)

        // test mesh
        // const testMesh = new THREE.Mesh(
        //     new THREE.BoxGeometry(1, 1, 1),
        //     new THREE.MeshStandardMaterial()

        // )
        // this.scene.add(testMesh)

        this.resources.on('ready', () =>
        {
            // console.log('resources are ready')

            //setup
            this.floor = new Floor()
            this.fox = new Fox()
            this.environment = new Environment()
            // this.floor = new Floor()  *** Put two lines above
        })

        // setup (moved above)
        // this.environment = new Environment()
    
    }
    update()
    {
        if(this.fox)
            this.fox.update()
    }
}