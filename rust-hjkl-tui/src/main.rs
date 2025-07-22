use std::{error::Error, io::stderr};

use app::App;
use ratatui::{backend::CrosstermBackend, crossterm::{event::{DisableMouseCapture, EnableMouseCapture}, execute, terminal::{disable_raw_mode, enable_raw_mode, EnterAlternateScreen, LeaveAlternateScreen}}, Terminal};

mod app;

fn main() -> Result<(), Box<dyn Error>> {
    enable_raw_mode()?;
    let mut stderr = stderr();
    execute!(stderr, EnterAlternateScreen, EnableMouseCapture)?;
    let mut terminal = Terminal::new(CrosstermBackend::new(stderr))?;
    terminal.clear()?;

    let mut app = App::default();


    while !app.exit {
        terminal.draw(|frame| {
            app.set_frame_size_limit(frame.size());
            frame.render_widget(&app, frame.size());
        })?;
        app.handle_event()?;
        app.update_char_position();
    }

    disable_raw_mode()?;
    execute!(
        terminal.backend_mut(),
        LeaveAlternateScreen,
        DisableMouseCapture,
    )?;
    terminal.clear()?;
    terminal.show_cursor()?;

    Ok(())
}
