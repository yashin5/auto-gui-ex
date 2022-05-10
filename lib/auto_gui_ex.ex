defmodule AutoGuiEx do
  @moduledoc """
  Documentation for `AutoGuiEx`.
  """
  alias AutoGuiEx.Python

  @doc """
  Call python function and handle it.

  ## Examples

      iex> AutoGuiEx.run(:position, [])
      %{x: 1229, y: 510}

  """
  @spec run(func :: atom(), pid :: pid() | nil, func_args :: list(), opts :: list()) :: any()
  def run(func, pid \\ nil, func_args \\ [], opts \\ []) do
    module = Keyword.get(opts, :module, :adapter)

    case pid do
      nil ->
        {:ok, new_pid} = Python.start_instance('python3')
        new_pid

      _ ->
        pid
    end
    |> Python.call_instance(module, func, func_args)
  end
end
