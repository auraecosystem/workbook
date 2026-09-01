#r "nuget: Azure.AI.OpenAI"
#r "nuget: Azure.Identity"
#r "nuget: Microsoft.Extensions.AI"

using Azure.AI.OpenAI;
using Azure.Identity;
using Microsoft.Extensions.AI;

public sealed class ScriptGodAgent
{
    private readonly IChatClient _chatClient;
    private readonly string _instructions;

    public ScriptGodAgent(
        string endpoint,
        string deploymentName,
        string instructions)
    {
        var client = new AzureOpenAIClient(
            new Uri(endpoint),
            new DefaultAzureCredential());

        _chatClient = client
            .GetChatClient(deploymentName)
            .AsIChatClient();

        _instructions = instructions;
    }

    public async Task<string> ExecuteAsync(string task)
    {
        var messages = new List<ChatMessage>
        {
            new(
                ChatRole.System,
                _instructions),

            new(
                ChatRole.User,
                task)
        };

        var response = await _chatClient
            .GetResponseAsync(messages);

        return response.Text ?? string.Empty;
    }
}


// Configuration
var endpoint =
    Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT")
    ?? throw new InvalidOperationException(
        "AZURE_OPENAI_ENDPOINT is not set.");

var deployment =
    Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT_NAME")
    ?? throw new InvalidOperationException(
        "AZURE_OPENAI_DEPLOYMENT_NAME is not set.");


// Agent definition
var agent = new ScriptGodAgent(
    endpoint,
    deployment,
    """
    You are an LMLM execution agent operating under SCRIPT.GOD.

    Protocol:
      REGISTER
      CAPABILITIES
      CONNECT
      ROUTE
      INSTRUCT
      CONTEXT
      TASK
      PROGRESS
      RESULT
      VERIFY
      SYNC
      ERROR
      BLOCKED
      CANCEL

    Execution rules:
      1. Understand the task.
      2. Determine required capabilities.
      3. Execute only authorized operations.
      4. Produce structured results.
      5. Verify the result before returning it.
      6. Report errors explicitly.
      7. Never claim an operation was completed unless it actually was.

    You are one interchangeable model adapter inside LMLM.
    SCRIPT.GOD is the authoritative orchestration layer.
    """);


// Execute
var result = await agent.ExecuteAsync(
    "Analyze this task and return the required execution plan.");

Console.WriteLine(result);
