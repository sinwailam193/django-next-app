"use client";

export default function Home() {
    async function getData() {
        const response = await fetch("/api/waitlist").then((res) => res.json());
        console.log(response);
    }

    return <button onClick={getData}>look up data</button>;
}
