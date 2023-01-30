import React, { useEffect, useState } from 'react'

const WS_URL = process.env.WS_URL ?  `ws://${process.env.WS_URL}` : 'ws://localhost:9696'

const MapRenderer = () => {
    const [websocket, setWebSocket] = useState(new WebSocket(WS_URL))
    const [mapMarkers, setMapMarkers] = useState([])

    useEffect(() => {
        //Register websocket events
        websocket.onopen = () => {
            console.log("opened");
        };

        websocket.onclose = () => {
            console.log("closed");
        };

        websocket.onmessage = ((event) => {
            console.log("got message", event.data)
            setMapMarkers(prevMarkers => {
                console.log(`Calling set Map Markers.... existing mapMarkers ${prevMarkers}`)
                return [...prevMarkers, event.data]
            })
        })
    }, [])

    return (
        <div>
            <h1>MAP COMPONENT</h1>
            {
                mapMarkers.map((marker, index) =>
                    <p key={index}>{marker}</p>
                )
            }
        </div>
    )
}

export default MapRenderer
