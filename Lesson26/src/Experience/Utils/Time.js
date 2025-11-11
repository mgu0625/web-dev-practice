import EventEmitter from './EventEmitter.js'

export default class Time extends EventEmitter
{
    constructor()
    {
        super()
        // console.log('Time instantiated')

        // setup
        this.start = Date.now()
        // console.log(this.start)
        this.current = this.start
        this.elapsed = 0

        this.delta = 16

        this.tick()

    }

    tick()
    {
        // console.log('tick')

        const currentTime = Date.now()
        this.delta = currentTime - this.current
        // console.log(this.delta)
        this.current = currentTime
        this.elapsed = this.current - this.start

        this.trigger('tick')


        window.requestAnimationFrame(() =>
        {
            this.tick()
        }
    )}
}