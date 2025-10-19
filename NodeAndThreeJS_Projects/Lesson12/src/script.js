import * as THREE from 'three'
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js'
import GUI from 'lil-gui'
// import typefaceFont from 'three/examples/fonts/helvetiker_regular.typeface.json'
import { FontLoader } from 'three/examples/jsm/loaders/FontLoader.js'
import { TextGeometry } from 'three/addons/geometries/TextGeometry.js';


/**
 * Base
 */
// Debug
const gui = new GUI()

// Canvas
const canvas = document.querySelector('canvas.webgl')

// Scene
const scene = new THREE.Scene()


/**
 * Textures
 */
const textureLoader = new THREE.TextureLoader()
const matcapTexture = textureLoader.load('/textures/matcaps/5.png')
matcapTexture.colorSpace = THREE.SRGBColorSpace

/**
 * fonts
 */
const fontLoader = new FontLoader()

fontLoader.load(
    '/fonts/helvetiker_regular.typeface.json',
    (font) =>
    {
        const textGeometry = new TextGeometry(
            'always in between\n the how and why',
            {
                font: font,
                size: 0.5,
                depth: 0.2,
                curveSegments: 6,
                bevelEnabled: true,
                bevelThickness: 0.03,
                bevelSize: 0.02,
                bevelOffset: 0,
                bevelSegments: 4
            } 
        )
        textGeometry.center()


        const material = new THREE.MeshMatcapMaterial({ matcap: matcapTexture })
        const text = new THREE.Mesh(textGeometry, material)
        scene.add(text)

        // exclusion sphere around text
        textGeometry.computeBoundingSphere()

        const textCenterWorld = text.localToWorld(textGeometry.boundingSphere.center.clone())
        const exclusionRadius = textGeometry .boundingSphere.radius + 1.0
        const spreadRange = 10


        function addRandomObjects(count, geometry, material) {

            for(let i = 0; i < 100; i++) {
                const mesh = new THREE.Mesh(geometry, material)
                mesh.position.x = (Math.random() - 0.5) * 10
                mesh.position.y = (Math.random() - 0.5) * 10
                mesh.position.z = (Math.random() - 0.5) * 10
                mesh.rotation.x = Math.random() * Math.PI
                mesh.rotation.y = Math.random() * Math.PI
                const scale = Math.random() * 0.8 + 0.2 
                mesh.scale.set(scale, scale, scale)
                scene.add(mesh)
            }
        }

        const diamondShape = new THREE.Shape()
        diamondShape.moveTo(0, 1)
        diamondShape.lineTo(0.6, 0)
        diamondShape.lineTo(0, -1)
        diamondShape.lineTo(-0.6, 0)
        diamondShape.lineTo(0, 1)
        const diamondGeometry = new THREE.ExtrudeGeometry(diamondShape, {
            depth: 0.1,
            bevelEnabled: false
        })

        const heartShape = new THREE.Shape()
        heartShape.moveTo(0, 0)
        heartShape.bezierCurveTo(0, 0.4, -0.5, 0.5, -0.5, 0)
        heartShape.bezierCurveTo(-0.5, -0.5, 0, -0.75, 0, -1)
        heartShape.bezierCurveTo(0, -0.75, 0.5, -0.5, 0.5, 0)
        heartShape.bezierCurveTo(0.5, 0.5, 0, 0.4, 0, 0)
        const heartGeometry = new THREE.ExtrudeGeometry(heartShape, {
            depth: 0.1,
            bevelEnabled: false
        })

        const clubShape = new THREE.Shape()
        const circle1 = new THREE.Path()
        circle1.absarc(0, 0.35, 0.3, 0, Math.PI * 2, false)
        clubShape.add(circle1)
        clubShape.moveTo(-0.4, -0.1)
        clubShape.absarc(-0.4, -0.1, 0.25, 0, Math.PI * 2, false)
        clubShape.moveTo(0.4, -0.1)
        clubShape.absarc(0.4, -0.1, 0.25, 0, Math.PI * 2, false)
        const clubGeometry = new THREE.ExtrudeGeometry(clubShape, {
            depth: 0.1,
            bevelEnabled: false
        })

        const spadeShape = new THREE.Shape()
        spadeShape.moveTo(0, 0)
        spadeShape.bezierCurveTo(0, -0.4, -0.5, -0.5, -0.5, 0)
        spadeShape.bezierCurveTo(-0.5, 0.5, 0, 0.8, 0, 1)
        spadeShape.bezierCurveTo(0, 0.8, 0.5, 0.5, 0.5, 0)
        spadeShape.bezierCurveTo(0.5, -0.5, 0, -0.4, 0, 0)
        const spadeGeometry = new THREE.ExtrudeGeometry(spadeShape, {
            depth: 0.1,
            bevelEnabled: false
        })

        addRandomObjects(25, diamondGeometry, material)
        addRandomObjects(25, heartGeometry, material)
        addRandomObjects(25, clubGeometry, material)
        addRandomObjects(25, spadeGeometry, material)
    }
)


/**
 * Object
 */
// const cube = new THREE.Mesh(
//     new THREE.BoxGeometry(1, 1, 1),
//     new THREE.MeshBasicMaterial()
// )

// scene.add(cube)

/**
 * Sizes
 */
const sizes = {
    width: window.innerWidth,
    height: window.innerHeight
}

window.addEventListener('resize', () =>
{
    // Update sizes
    sizes.width = window.innerWidth
    sizes.height = window.innerHeight

    // Update camera
    camera.aspect = sizes.width / sizes.height
    camera.updateProjectionMatrix()

    // Update renderer
    renderer.setSize(sizes.width, sizes.height)
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))
})

/**
 * Camera
 */
// Base camera
const camera = new THREE.PerspectiveCamera(75, sizes.width / sizes.height, 0.1, 100)
camera.position.x = 1
camera.position.y = 1
camera.position.z = 2
scene.add(camera)

// Controls
const controls = new OrbitControls(camera, canvas)
controls.enableDamping = true

/**
 * Renderer
 */
const renderer = new THREE.WebGLRenderer({
    canvas: canvas
})
renderer.setSize(sizes.width, sizes.height)
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))

/**
 * Animate
 */
const clock = new THREE.Clock()

const tick = () =>
{
    const elapsedTime = clock.getElapsedTime()

    // Update controls
    controls.update()

    // Render
    renderer.render(scene, camera)

    // Call tick again on the next frame
    window.requestAnimationFrame(tick)
}

tick()