import arg from 'arg';

function parseArguments(raw) {
    const args = arg(
        {
            '-t': '--type',
            '-d': '--directory'
        },
        {
            argv: raw.slice(2)
        }
    );
    return {
        skipPrompts: args['--yes'] || false,
        git
    }
};

export function cli(args) {
    let options = parseArguments(args);
    console.log(options);
}