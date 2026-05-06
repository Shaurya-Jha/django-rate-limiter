<script lang="ts">
    import type { PageProps } from "./$types";

    const {data}: PageProps = $props();
</script>

<div>
    <p>Welcome to all tasks</p>

    {#each data.data as task, index(index)}
    <p>{task.title}</p>
    {/each}
</div>