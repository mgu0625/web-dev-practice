uniform mat4 projectionMatrix;
// uniform mat4 modelViewMatrix;
uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform vec2 uFrequency;
uniform float uTime;

attribute vec3 position;
// attribute float aRandom;
attribute vec2 uv;

varying vec2 vUv;
varying float vElevation;

// varying float vRandom;

void main()
{
    // gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);

    vec4 modelPosition = modelMatrix * vec4(position, 1.0);

    float elevation = sin(modelPosition.x * uFrequency.x - uTime) * 0.1;

    // modelPosition.y = += 1.0;

    modelPosition.z += sin(modelPosition.x * uFrequency.x + uTime) * 0.1;
    modelPosition.z += sin(modelPosition.y * uFrequency.y - uTime ) * 0.1;
    // modelPosition.z += aRandom * 0.1;

    // modelPosition.y += uTime;


    vec4 viewPosition = viewMatrix * modelPosition;
    vec4 projectedPosition = projectionMatrix * viewPosition;

    // gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
    gl_Position = projectedPosition;

    // vRandom = aRandom;

    vUv = uv; 
    vElevation = elevation;

}