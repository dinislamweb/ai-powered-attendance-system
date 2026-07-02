export default function Button({
  text,
  loading = false,
}) {
  return (
    <button
      type="submit"
      disabled={loading}
      className="
      w-full
      rounded-xl
      bg-blue-600
      py-3
      text-white
      font-semibold
      transition-all
      duration-300
      hover:bg-blue-700
      active:scale-95
      disabled:cursor-not-allowed
      disabled:bg-blue-400
      "
    >
      {loading ? "Logging in..." : text}
    </button>
  );
}