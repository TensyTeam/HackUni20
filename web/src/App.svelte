<script>
	import Search from './Search.svelte';

	let status = 0;
	let text = '';

	function search() {
		status = 1;
	}
</script>

<main>
	<Search
		status={status}
		bind:text={text}
		on:click={search}
	/>
</main>