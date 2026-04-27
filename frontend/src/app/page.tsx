export default function Home() {
  return (
    <div className="flex min-h-screen items-center justify-center bg-zinc-50 p-8 dark:bg-zinc-950">
      <main className="w-full max-w-2xl rounded-lg border border-zinc-200 bg-white p-8 shadow-sm dark:border-zinc-800 dark:bg-zinc-900">
        <h1 className="mb-3 text-3xl font-semibold text-zinc-900 dark:text-zinc-100">
          Grant Platform
        </h1>
        <p className="mb-6 text-zinc-600 dark:text-zinc-400">
          Phase 1 shell is running. Frontend, backend, database, Redis, and worker are connected.
        </p>
        <div className="rounded-md bg-zinc-100 p-4 text-sm text-zinc-700 dark:bg-zinc-800 dark:text-zinc-200">
          <p>API base URL: {process.env.NEXT_PUBLIC_API_BASE_URL}</p>
          <p>Health endpoint: /health</p>
        </div>
      </main>
    </div>
  );
}
