import type { PageLoad } from "./$types";

export const load: PageLoad = () => {
    const data = fetch("localhost:8000/api/v1/tasks/all").then((res) => res).catch(err => err);

    return data;
}