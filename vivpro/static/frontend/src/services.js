import { getCookie } from "./helpers";

export const getMusicTracks = async (page_no = 1) => {
    let url = `/api/tracks/fetch-by-page/${page_no}/1`
    let response = await fetch(url);
    return await response.json();
}

export const rateSong = async (trackId, rating) => {
    let url = `/api/tracks/rate/${trackId}`;
    let response = await fetch(url, {
        method: "POST",
        body: JSON.stringify({ rating }),
        headers: {
            "Content-type": "application/json; charset=UTF-8",
            'X-csrftoken': getCookie('csrftoken')
        }
    });
    alert("Successful!")
    return await response.json();
}
