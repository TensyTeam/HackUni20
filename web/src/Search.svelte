<script>
	import ClickOutside from 'svelte-click-outside';

	export let status, text;

	let innerEl;

	function search() {
		status = 1;
	}

    function outsearch() {
		if (text.length) {
			status = 3;
		} else {
			if (status !== 0) {
				status = 2;
			}
		}
    }
</script>

<div class={status === 0 ? 'start' : status === 2 ? 'start start-back' : 'start start-extra'}>
	<div>
		<ClickOutside on:clickoutside={outsearch} exclude={[innerEl]}>
			<input
				placeholder={status === 1 ? 'Поиск' : "Привет 😉"}
				bind:value={text}
				on:click={search}
				bind:this={innerEl}
			/>
		</ClickOutside>
	</div>
</div>

<style>
	.start {
		position: fixed;
		top: 0;
		left: 0;
		text-align: center;
		width: 100vw;
		height: 100vh;
		line-height: 85vh;
	}

	.start-extra {
		animation: display 1s 1;
		animation-fill-mode: forwards;
	}

	.start-back {
		top: 25px;
		line-height: 1rem;
		animation: display-back 1s 1;
		animation-fill-mode: forwards;
	}

	@keyframes display {
		100% {
			top: 25px;
			line-height: 1rem;
		}
	}

	@keyframes display-back {
		100% {
			top: 0;
			line-height: 85vh;
		}
	}

	.start div {
		line-height: 1rem;
	}

	.start input {
		padding: 10px 15px;
		border: 1.5px solid #333;
		border-radius: 15px;
		width: 80vw;
		min-width: 250px;
		max-width: 550px;
		font-size: 1.4rem;
		font-weight: 420;
		background-color: #fff;
		outline: none;
		caret-color: #000;
		box-shadow:
			0 1px 4px rgba(0, 0, 0, .3),
			-23px 0 20px -23px rgba(0, 0, 0, .8),
			13px 0 20px -23px rgba(0, 0, 0, .8);
	}
</style>
