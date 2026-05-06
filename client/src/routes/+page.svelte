<script lang="ts">
	function handleSubmit() {
		window.location.assign('/all-tasks');
	}
</script>

<div class="flex h-screen w-screen flex-col items-center justify-center gap-4">
	<p>Welcome to Taskinator</p>

	<button class="hover:cursor-pointer" onclick={handleSubmit}>Go to my tasks</button>
</div>
