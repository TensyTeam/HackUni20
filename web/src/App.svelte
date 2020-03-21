<script>
	import Search from './Search.svelte';

	let status = 0;

	function changeStatus(event) {
		status = event.detail.cont;
	}
</script>

<main>
	<Search on:changeStatus={changeStatus} />
</main>

<style>
	main {
		padding: 8px;
	}
</style>
